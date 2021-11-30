import React from 'react';
import {ReactComponent as Logo} from '../../Asset/Logo.svg';
import {IconButton, AppBar, makeStyles, Toolbar, Button, styled, Typography, Grid } from '@material-ui/core';
import { withRouter } from 'react-router-dom';
import { purple } from '@material-ui/core/colors';
import  './Header.css';
import makeStyle from '@material-ui/core';
import { border, Box, grid } from '@mui/system';
import { Stack } from '@mui/material';

const useStyles = makeStyles(() => ({
    header: {
        backgroundColor: "#ffffff",
    },
}));

const ColorButton = styled(Button)(({ theme }) => ({
  color: theme.palette.getContrastText(purple[500]),
  backgroundColor: purple[500],
  '&:hover': {
    backgroundColor: purple[700],
  },
}));



const Header = props => {
    const { header } = useStyles();
    const { history } = props;
    const [anchorEl, setAnchorEl] = React.useState(null);

    const handleMenu = event => {
      setAnchorEl(event.currentTarget);
    };

    const handleButtonClick = pageURL =>{
      history.push(pageURL);
    };

    const menuItems = [
      {
        menuTitle: "Home",
        pageURL: "/"
      },
      {
        menuTitle: "Login",
        pageURL: "/login"
      },
      {
        menuTitle: "Signup",
        pageURL: "/signup"
      },
      {
        menuTitle: "About",
        pageURL: "/about"
      }
    ];

  return (
    <header>
      <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" className={header}>
        <Toolbar>
          <Grid
          justifyContent='center'
          direction='row'
          alignItems='center'
          container
          spacing={2}>
            <Grid item xs={4}
            align='left'>
              <IconButton
                size="large"
                edge="start"
                color="inherit"
                aria-label="menu"
                sx={{ mr: 5 }}
              >
              <Logo/>
              </IconButton>
              
              </Grid>
              <Grid item xs={4}>
                  <Stack direction='row' spacing={2} justifyContent='center'>
                    <Button
                    onClick={() => handleButtonClick("/")}>
                      Home
                    </Button>
                    <Button
                    onClick={() => handleButtonClick("/about")}>
                      About
                    </Button>
                  </Stack>
                  
              </Grid>
            
              <Grid item xs={4} >
                <Stack direction="row" spacing={2} justifyContent='flex-end'>
                  <ColorButton 
                  onClick={() => handleButtonClick("/login")}>Login</ColorButton>
                  <Button variant='outlined'
                  onClick={() => handleButtonClick("/signup")}>sign up</Button>
                </Stack>
              </Grid>
            </Grid>
        </Toolbar>
      </AppBar>
    </Box>
      
    </header>
  );
}
export default withRouter(Header);