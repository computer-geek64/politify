import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Alert from '@material-ui/lab/Alert';
import { useForm } from "react-hook-form";
import axios from 'axios';

function MainForm() {
    // const [show]

    const { register, handleSubmit, reset} = useForm();
    const onSubmit = data => {
        var config = {
            method: 'post',
            url: 'http://47.203.181.231:8000/people/new/',
            headers: { 
              'Content-Type': 'application/json'
            },
            data : data
        };

        axios(config)
        .then(function(response) {
            alert("You have sucessfully submitted the handle " + data['handle'] + "! Please be patient while our ML algorithm processes the account's tweets")            
        })
        .catch(function (error) {
            console.log(error);
        });
        reset();
    }

    return (
        <div className="mainform-container">
            <div className="caption">
            <Typography variant="h3">Enter a user's twitter handle to see how<br/>
            politically <font className="special-font">biased</font> their tweets are.</Typography>
            </div>
            <form className="main-form" onSubmit={handleSubmit(onSubmit)}>
                <TextField name="handle" inputRef={register} id="outlined-basic" label="Twitter Handle" variant="outlined" defaultValue="@" width={500}/>
                <div className="form-button"><Button type="submit" variant="outlined" color="secondary">Submit</Button></div>
            </form>
            {/* <Alert severity="success">This is a success alert — check it out!</Alert> */}
        </div>
    )
}

export default MainForm;