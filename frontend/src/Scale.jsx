import React from 'react';

function Scale(props) {
    const scaleStyle = {
        width: props.score/100 * 600,
    }

    return (
        <div className="scale-main">
            <div style={scaleStyle}></div>
            <div className="scale-marker"></div>
        </div>
    )
}

export default Scale;