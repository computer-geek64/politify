import React, {useState} from 'react';
import Popover from '@material-ui/core/Popover';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import HoverCard from './HoverCard';

const useStyles = makeStyles((theme) => ({
    popover: {
      pointerEvents: 'none',
    },
    paper: {
      padding: theme.spacing(1),
    },
  }));

function ScaleMarker(props) {
    const classes = useStyles();
    const [anchorEl, setAnchorEl] = useState(null);
    
    const handlePopoverOpen = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handlePopoverClose = () => {
        setAnchorEl(null);
    };

    const open = Boolean(anchorEl);

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
            <div aria-owns={open ? 'mouse-over-popover' : undefined}
            aria-haspopup="true"
            onMouseEnter={handlePopoverOpen}
            onMouseLeave={handlePopoverClose} >
            <a href="#"><img src={props.image} className="scale-marker"></img></a>
            <Popover
                id="mouse-over-popover"
                className={classes.popover}
                open={open}
                anchorEl={anchorEl}
                anchorOrigin={{
                    vertical: 'top',
                    horizontal: 'center',
                }}
                transformOrigin={{
                    vertical: 'bottom',
                    horizontal: 'center',
                }}
                onClose={handlePopoverClose}
                disableRestoreFocus
            >
                <HoverCard name={props.name} image={props.image} alt={props.alt}/>
            </Popover>
            </div>
        </div>
    )
}

export default ScaleMarker;