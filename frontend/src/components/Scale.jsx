import React from 'react';
import ScaleMarker from './ScaleMarker';

function Scale() {
    return (
        <div className="scale-main">
            <ScaleMarker score={10}/>
            <ScaleMarker score={20}/>
        </div>
    )
}

export default Scale;