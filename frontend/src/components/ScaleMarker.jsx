import React from 'react';

function ScaleMarker(props) {
    const containerStyle = {
        position: 'relative',
        display: 'flex',
        alignItems: 'center',
    }

    const scaleStyle = {
        width: props.score/100 * 600 - 10,
    }

    return (
        <div style={containerStyle}>
            <div style={scaleStyle}></div>
            <img className="scale-marker"></img>
        </div>
    )
}

export default ScaleMarker;