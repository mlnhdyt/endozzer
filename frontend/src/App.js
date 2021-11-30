import React from 'react';
import { Switch, Route, BrowserRouter as Router } from 'react-router-dom';

import Header from './component/header/Header';
import Login from './view/login/Login';
import About from './view/About';
import Signup from './view/Signup'
import Utama from './view/Utama';
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({});

export default function App(){
  const classes = useStyles();
  return(
    <div className={classes.container}>
      <Router>
          <Header />
        <Switch>
          <Route exact from="/" render={props => <Utama {...props} />} />
          <Route exact from="/login" render={props => <Login {...props} />} />
          <Route exact from="/signup" render={props => <Signup {...props} />} />
          <Route exact from="/about" render={props => <About {...props} />} />
        </Switch>
      </Router>
      
    </div>
    
  )
}


