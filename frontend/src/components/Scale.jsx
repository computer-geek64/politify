import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ScaleMarker from './ScaleMarker';

function Scale() {
    const [data, setData] = useState(null);
    const [min, setMin] = useState(0);
    const [max, setMax] = useState(0);

    var config = {
        method: 'get',
        url: 'http://47.201.32.187:8000/people/',
    };
        

    useEffect(() => {
        async function redemption() {
            let response = await  axios(config);
            setMin(response.data['min']);
            setMax(response.data['max']);
            setData(response.data['people']);
        } 

        if (data == null) {
            redemption();
        } 
    }, [data])

    return (
        <div className="scale-main">
            {
                data && data.map((item) => <ScaleMarker score={(item['score']/(max - min)) * 100} name={item['name']} alt={item['handle']} image={item['picture']}/>)
            }
        </div>
    )
}

export default Scale;