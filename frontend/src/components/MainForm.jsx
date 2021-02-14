import React from 'react';
import TextField from '@material-ui/core/TextField';
import { useForm } from "react-hook-form";
import axios from 'axios';

function MainForm() {
    const { register, handleSubmit, } = useForm();

    const onSubmit = data => {
        var config = {
            method: 'post',
            url: 'http://47.201.32.187:8000/people/new/',
            headers: { 
              'Content-Type': 'application/json'
            },
            data : data
        };

        axios(config)
        .then(function (response) {
            console.log(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
        });
    }

    return (
        <div className="App-header">
            Enter a user's twitter handle to see how biased their tweets are.
            <form onSubmit={handleSubmit(onSubmit)}>
                <TextField name="handle" inputRef={register} id="outlined-basic" label="Twitter Handle" variant="outlined" defaultValue="@"/>
            </form>
        </div>
    )
}

export default MainForm;