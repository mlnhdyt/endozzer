import React, {useState, useContext} from "react";
import clsx from 'clsx';
import {Button, FormControl, Grid, makeStyles, Paper, TextField, Typography} from '@material-ui/core';
import { Box } from "@mui/system";
import { Stack } from '@mui/material';
import { AuthContext } from "../../auth";
import { useHistory } from "react-router";
import axios from "axios";
import { Redirect } from "react-router";
import { ThemeContext } from "@mui/styled-engine";
import { Route } from "react-router";

const useStyles = makeStyles((theme) => ({
    root:{
        display: 'flex',
        flexWrap: 'wrap',
    },
    margin:{
        margin: theme.spacing(1),
    },
    textField:{
        marginTop: 20,
        marginBottom: 20,
        display: 'block',
    },
    paperBox:{
        elevation: 10,
        padding: 20,
        display: 'flex',
        flexDirection:"column",
        flexWrap: 'wrap',
        height:'370px', 
        width:'700px',
        margin:'100px auto',
        backgroundColor: '#F7EFFC',
    },
}));

export default function Login(){
    const style = useStyles();
    const [error, setError] = useState(null);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    

    //const { isAuthenticated, loginSuccess, loginFailed } = useContext(AuthContext);
    
    const history = useHistory();

    async function handleButtonSubmit(event) {
        event.preventDefault();
        console.warn(username, password);
        var data = {username,password};

        var hasil = await fetch("/api/auth/token/",{
            //credentials:'include',
            method:'POST',
            headers:{
                'Content-Type': "application/json",
                'Accept': 'application/json',
            },
            body: JSON.stringify(data)
        });

        hasil = await hasil.json();
        console.log(hasil)
        localStorage.setItem("user-info", JSON.stringify(hasil));
        history.push('/about')
        // axios(hasil)
        // .then(function (response){
        //     console.log(response.hasil);
        //     localStorage.setItem("user-info", JSON.stringify(response))
        //     loginSuccess();
        // })
        // .catch(function (error){
        //     console.log(error);
        //     setUsername("")
        //     setPassword("")
        //     loginFailed()
        // });

        // if (isAuthenticated){   
        //     localStorage.setItem("isLogin", isAuthenticated) 
        //     console.log("di if " + isAuthenticated)
        //     return <Redirect to={{
        //       pathname: "/home",
        //       state: {
        //         username: username
        //       }
        //     }} />
        // };
    }
   
    return(
   
        <Paper className={style.paperBox}>
            <Typography variant='h5' component="div" gutterBottom align='center'>Login as influencer</Typography>
            <form noValidate autoComplete='off'>
                <Typography variant='body1' component="div" gutterBottom>Username</Typography>
                <TextField  
                    className={style.textField}
                    variant='outlined'
                    placeholder='Masukkan Username'
                    fullWidth 
                    onChange={e => setUsername(e.target.value)}/>
                <Typography variant='body1' component="div" gutterBottom>Password</Typography>
                <TextField  
                    className={style.textField}
                    variant='outlined'
                    type='password' 
                    placeholder='Password'
                    fullWidth
                    onChange={e => setPassword(e.target.value)}/>
                    <Stack direction="column" spacing={2} justifyContent='center' alignItems='center'>
                        <Button
                            type='submit'
                            variant='contained'
                            style={{backgroundColor: '#8122B3',
                                color: '#ffffff'}}
                            onClick={handleButtonSubmit}>
                                Login
                        </Button>
                   
                        <Typography>
                            Don’t have an account? Sign Up
                        </Typography>
                   </Stack> 
            </form>
            {error && <p className='error'>{error}</p>}
        </Paper>
        
    )
}

