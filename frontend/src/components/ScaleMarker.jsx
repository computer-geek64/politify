import React, {useEffect, useState} from 'react';
import wiki from 'wikijs';

import Popover from '@material-ui/core/Popover';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import HoverCard from './HoverCard';

import Dialog from '@material-ui/core/Dialog';
import MuiDialogTitle from '@material-ui/core/DialogTitle';
import MuiDialogContent from '@material-ui/core/DialogContent';
import DialogActions from '@material-ui/core/DialogActions';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Avatar from '@material-ui/core/Avatar';


const useStyles = makeStyles((theme) => ({
    popover: {
      pointerEvents: 'none',
    },
}));

const styles = (theme) => ({
    root: {
      margin: 0,
      padding: theme.spacing(2),
    },
    closeButton: {
      position: 'absolute',
      right: theme.spacing(1),
      top: theme.spacing(1),
      color: theme.palette.grey[500],
    },
});

const DialogTitle = withStyles(styles)((props) => {
    const { children, classes, onClose, ...other } = props;
    return (
        <MuiDialogTitle disableTypography className={classes.root} {...other}>
        <Typography variant="h6">{children}</Typography>
        </MuiDialogTitle>
    );
});

const DialogContent = withStyles((theme) => ({
    root: {
        padding: theme.spacing(2),
    },
}))(MuiDialogContent);

function ScaleMarker(props) {
    const classes = useStyles();
    const [anchorEl, setAnchorEl] = useState(null);
    const [dialogOpen, setDialogOpen] = useState(false);
    const [information, setInformation] = useState(null)

    useEffect(() => {
        async function loadInformation() {
            let str = ""
            wiki().page(props.name)
                .then(page => page.summary())
                .then(item => {
                    str = item
                    str = str.replace(/\s*\(.*?\)\s*/g, '')
                    str = str.split('\n')[0];
                    setInformation(str); 
                })
                .catch(function (error) {
                    setInformation("No discription avaliable")
                });
        }

        if(information == null) loadInformation();

    }, [information, setInformation])

    const handleClickOpen = () => {
        setDialogOpen(true);
        setAnchorEl(null);
    };
    const handleClose = () => {
        setDialogOpen(false);
    };

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
        width: props.score * window.innerWidth * 0.6,
    }

    return (
        <div style={containerStyle}>
            <div style={scaleStyle}></div>
            <div aria-owns={open ? 'mouse-over-popover' : undefined}
            aria-haspopup="true"
            onMouseEnter={handlePopoverOpen}
            onMouseLeave={handlePopoverClose} >
            <div onClick={handleClickOpen}><img src={props.image} className="scale-marker"></img></div>
            <Dialog onClose={handleClose} aria-labelledby="customized-dialog-title" open={dialogOpen}>
            <DialogTitle id="customized-dialog-title" onClose={handleClose}>
                <div className="title-box">
                    <Typography variant="h5">{props.name}</Typography>
                    <Avatar alt={props.handle} src={props.image} className={classes.large} />
                </div>
            </DialogTitle>
            <DialogContent dividers>
            <Typography variant="h6" gutterBottom>
                {information}
            </Typography>
            <Typography gutterBottom>
                <font className="special-font">Bias score: {props.score * 100}</font>
            </Typography>
            </DialogContent>
            <DialogActions>
            <Button autoFocus onClick={handleClose} color="primary">
                Close
            </Button>
            </DialogActions>
        </Dialog>
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