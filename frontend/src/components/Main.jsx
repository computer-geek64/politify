import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import Toolbar from '@material-ui/core/Toolbar';
import Avatar from '@material-ui/core/Avatar';
import { createMuiTheme, ThemeProvider} from '@material-ui/core/styles';

import About from './About.jsx';
import MainForm from './MainForm';
import Scale from './Scale.jsx';
import TweetForm from './Tweetform.jsx';

const darkTheme = createMuiTheme({
  palette: {
    type: 'dark',
  },
  typography: {
    fontFamily: [
      'Poppins',
      'sans-serif',
    ].join(','),
    button: {
      textTransform: 'none',
    },
  },
});

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`nav-tabpanel-${index}`}
      aria-labelledby={`nav-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `nav-tab-${index}`,
    'aria-controls': `nav-tabpanel-${index}`,
  };
}

function LinkTab(props) {
  return (
    <Tab
      component="a"
      onClick={(event) => {
        event.preventDefault();
      }}
      {...props}
    />
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
  },
  title: {
    flexGrow: 1,
  },
}));

export default function Main(props) {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <ThemeProvider theme={darkTheme}>
      <AppBar position="fixed">
        <Box display="flex" alignItems="center" justifyContent="space-between" padding={0}>
        <Toolbar>
          <Avatar alt="politify" src={props.image} className={classes.large}/>
          <Typography variant="h5" style={{paddingLeft: '0.5vw'}}>Politify</Typography>
        </Toolbar>
        <Tabs
          value={value}
          onChange={handleChange}
          aria-label="nav tabs example"
        >
          <LinkTab label="About" {...a11yProps(0)} />
          <LinkTab label="pol(@anyone)"  {...a11yProps(1)} />
          <LinkTab label="Politi-scale" {...a11yProps(2)} />
          <LinkTab label="Your Tweet!" {...a11yProps(3)} />
        </Tabs>
        </Box>
      </AppBar>
      <div className="App-header">
        <TabPanel value={value} index={0}>  
          <About />
        </TabPanel>
        <TabPanel value={value} index={1}>
          <MainForm/>           
        </TabPanel>
        <TabPanel value={value} index={2}>
          <Scale/>
        </TabPanel>
        <TabPanel value={value} index={3}>
          <TweetForm/>
        </TabPanel>
      </div>
      </ThemeProvider>
    </div>
  );
}
