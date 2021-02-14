import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Typography from '@material-ui/core/Typography';
import ScaleMarker from './ScaleMarker';

function Scale() {
    const [data, setData] = useState(null);
    const [min, setMin] = useState(0);
    const [max, setMax] = useState(0);
    const [total, setTotal] = useState(0);

    var config = {
        method: 'get',
        url: 'http://47.203.181.231:8000/people/',
    };
        

    useEffect(() => {
        async function redemption() {
            let response = await  axios(config);
            setMin(response.data['min']);
            setMax(response.data['max']);
            setData(response.data['people']);
            let score = 0;
            response.data['people'].forEach((item) => score = score + item['score'])
            setTotal(score)
        } 

        if (data == null) {
            redemption();
        } else {
            console.log(total)
        }
    }, [data])

    return (
        <div className="scale-container">
            <div className="invisible-container">
            <div className="scale-info">
                <Typography variant="h2"><font className="special-font">The political spectrum</font></Typography>
                <Typography variant="h6">
                    This spectrum tries to quantify how "radical" politicians' <br/>
                    tweets are relative to their colleagues. The scale realigns itself <br/>
                    every time a user adds an additional public figure.
                </Typography>
            </div>

            <div className="scale-main-container">
                <div className="markers">
                    <Typography>Strongly Liberal</Typography>
                    <Typography>Liberal</Typography>
                    <Typography>Neutral</Typography>
                    <Typography>Conservative</Typography>
                    <Typography>Strongly Conservative</Typography>
                </div>
                <div className="scale-main">
                    {
                        data && data.map((item) => <ScaleMarker score={(item['score'] - min)/(max - min)} name={item['name']} alt={item['handle']} image={item['picture']}/>)
                    }
                </div>
            </div>
            </div>
        </div>
    )
}

export default Scale;