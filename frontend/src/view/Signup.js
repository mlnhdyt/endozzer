import React, {useState, useContext} from "react";
import clsx from 'clsx';
import {Button, FormControl, Grid, makeStyles, Paper, TextField, Typography} from '@material-ui/core';
import { Box } from "@mui/system";
import { Stack } from '@mui/material';
import { AuthContext } from "../auth";
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
        height:'500px', 
        width:'700px',
        margin:'100px auto',
        backgroundColor: '#F7EFFC',
    },
}));


export default function Signup(){
    const style = useStyles();
    const [error, setError] = useState(null);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");

    //const { isAuthenticated, loginSuccess, loginFailed } = useContext(AuthContext);
    
    //const history = useHistory();

     function handleButtonSubmit(event) {
        event.preventDefault();
    }
   
    return(
   
        <Paper className={style.paperBox} >
            <Typography variant='h5' component="div" gutterBottom align='center'> Sign Up as Influencer</Typography>
            <form noValidate autoComplete='off'>
                <Typography variant='body1' component="div" gutterBottom>Email</Typography>
                <TextField  
                    className={style.textField}
                    variant='outlined'
                    placeholder='Masukkan Email'
                    fullWidth 
                    onChange={e => setEmail(e.target.value)}/>
                <Typography variant='body1' component="div" gutterBottom>Username</Typography>
                <TextField  
                    className={style.textField}
                    variant='outlined'
                    placeholder='Masukkan Username'
                    fullWidth 
                    onChange={e => setUsername(e.target.value)}/>
                <Grid container spacing={2} direction="row" >
                    <Grid item xs={6}> 
                        <Typography variant='body1' component="div">Password</Typography>
                    </Grid>
                    <Grid item xs={6}> 
                        <Typography variant='body1' component="div">Konfirmasi Password</Typography>
                    </Grid>
                    <Grid item xs={6}> 
                        <TextField  
                            className={style.textField}
                            variant='outlined'
                            type='password' 
                            placeholder='Password'
                            fullWidth
                            onChange={e => setPassword(e.target.value)}/>
                    </Grid>
                    <Grid item xs={6}>
                        <TextField  
                            className={style.textField}
                            variant='outlined'
                            type='password' 
                            placeholder='Konfirmasi passwordPassword'
                            fullWidth
                            onChange={e => setPassword(e.target.value)}/>
                    </Grid>
                </Grid>
                    <Stack direction="column" spacing={2} justifyContent='center' alignItems='center'>
                        <Button
                            type='submit'
                            variant='contained'
                            style={{backgroundColor: '#8122B3',
                                color: '#ffffff'}}
                            onClick={handleButtonSubmit}>
                                Login
                        </Button>
                   
                   </Stack> 
                
            </form>
            {error && <p className='error'>{error}</p>}
        </Paper>
        
    )

}

