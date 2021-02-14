import React from 'react';
import Typography from '@material-ui/core/Typography';
import mainGif from './images/vector.gif';

function About() {
    return (
        <div className="about-container">
            <div>
                <img className="about-vector" src={mainGif}></img>
                <div className="about-info">
                    <Typography variant="h2"><font className="special-font">Are you swayed?</font></Typography>
                    <Typography variant="h6">
                        Misinformation through social media is one the leading causes <br/>
                        of real life agression and "senseless" violence. Politify uses NLP to <br/>
                        combat misinformation and reveal biases among politicians while<br/>
                        reamining politically unbiased UNLIKE traditional news sources.
                    </Typography>
                </div>
            </div>
        </div>
    )
}

export default About;