import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { useForm } from "react-hook-form";
import axios from 'axios';

function TweetForm() {
    const { register, handleSubmit, reset} = useForm();
    const onSubmit = data => {
        var config = {
            method: 'post',
            url: 'http://47.203.181.231:8000/analyze/',
            headers: { 
              'Content-Type': 'application/json'
            },
            data : data
        };

        axios(config)
        .then(function(response) {
            let str = "liberal."
            if (response.data == 'Right') str = "conservative."
            alert('Your tweet "' + data['tweet'] + '" is more likely to be politically ' + str)            
        })
        .catch(function (error) {
            console.log(error);
        });
        reset();
    }

    return (
        <div className="tweetform-container">
            <div className="caption">
            <Typography variant="h3">Enter a sample tweet to see how politically <br/>
            <font className="special-font">biased</font> it may be.</Typography>
            </div>
            <form className="main-form" onSubmit={handleSubmit(onSubmit)}>
                <TextField name="tweet" inputRef={register({ required: true})} id="outlined-basic" label="Your Tweet" variant="outlined" width={500}/>
                <div className="form-button"><Button type="submit" variant="outlined" color="primary">Tweet</Button></div>
            </form>
        </div>
    )
}

export default TweetForm;