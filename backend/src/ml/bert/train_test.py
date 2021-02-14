#!/usr/bin/python3
# train_test.py

import os
import re
import torch
import random
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from transformers import Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from transformers import BertTokenizerFast, BertForSequenceClassification
from transformers.file_utils import is_tf_available, is_torch_available, is_torch_tpu_available


# Set seed to reproduce identical stochastic behavior in subsequent runs
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)

    if is_torch_available():
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    if is_tf_available():
        import tensorflow as tf
        tf.random.set_seed(seed)


def preprocess_text(text):
    # Makes text lowercase
    # Removes hyperlinks
    # Replaces newlines with spaces
    # Removes trailing spaces
    return re.sub(r'https?:\/\/.*[\r\n]*', '', text.lower()).replace('\n', ' ').strip()


def preprocess_dataset(filename=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datasets', 'ExtractedTweets.csv'), test_data_percentage=0.2):
    dataset = pd.read_csv(filename, sep=',')
    dataset = dataset.sample(frac=1).reset_index(drop=True)

    #data = list(dataset['Tweet'].apply(lambda x: ''.join(c for c in re.sub(r'https?:\/\/.*[\r\n]*', '', x.lower().replace('\n', ' ').replace('&amp;', 'and')) if c in 'abcdefghijklmnopqrstuvwxyz01234567890 ,.!?/$%()-').strip()))
    data = list(dataset['Tweet'].apply(lambda text: re.sub(r'^rt @.*: ', '', preprocess_text(text).replace('…', ''))))
    labels = np.array(dataset['Party'] == 'Democrat').astype(int)
    label_names = ['Republican', 'Democrat']

    return train_test_split(data, labels, test_size=test_data_percentage), label_names


class TorchDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, index):
        item = {k: torch.tensor(v[index]) for k, v in self.encodings.items()}
        item['labels'] = torch.tensor([self.labels[index]])
        return item

    def __len__(self):
        return len(self.labels)


def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)

    # Calculate accuracy through sklearn
    accuracy = accuracy_score(labels, preds)
    return {'accuracy': accuracy}


def train_model():
    set_seed(1)

    model_name = 'bert-base-uncased'
    max_length = 512

    tokenizer = BertTokenizerFast.from_pretrained(model_name, do_lower_case=True)

    (train_x, test_x, train_y, test_y), label_names = preprocess_dataset()

    train_encodings = tokenizer(train_x, truncation=True, padding=True, max_length=max_length)
    test_encodings = tokenizer(test_x, truncation=True, padding=True, max_length=max_length)

    train_dataset = TorchDataset(train_encodings, train_y)
    test_dataset = TorchDataset(test_encodings, test_y)

    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(label_names))#.to('cuda')

    training_arguments = TrainingArguments(
        output_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results'),
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=20,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs'),
        load_best_model_at_end=True,
        logging_steps=200,
        evaluation_strategy='steps'
    )

    trainer = Trainer(
        model=model,
        args=training_arguments,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        compute_metrics=compute_metrics
    )

    trainer.train()
    trainer.evaluate()

    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'political_tweets_bert-base-uncased_2')
    model.save_pretrained(model_path)
    tokenizer.save_pretrained(model_path)


def get_predictions(texts):
    set_seed(1)

    max_length = 512

    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'political_tweets_bert-base-uncased_1')
    tokenizer = BertTokenizerFast.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)

    #inputs = tokenizer([''.join(c for c in re.sub(r'https?:\/\/.*[\r\n]*', '', text.lower().replace('\n', ' ').replace('&amp;', 'and')) if c in 'abcdefghijklmnopqrstuvwxyz01234567890 ,.!?/$%()-').strip() for text in texts], padding=True, truncation=True, max_length=max_length, return_tensors='pt')
    inputs = tokenizer(list(map(preprocess_text, texts)), padding=True, truncation=True, max_length=max_length, return_tensors='pt')
    outputs = model(**inputs)
    return [['right', 'left'][output.argmax()] for output in outputs[0].softmax(1)]

