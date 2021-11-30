import React, {useState, useContext} from "react";
import clsx from 'clsx';
import {Button, FormControl, Grid, makeStyles, Paper, TextField} from '@material-ui/core';
import { Box } from "@mui/system";

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
        backgroundColor: '#F2F2F2',
    },
}));

const Login=() =>{
    const style = useStyles();
    const [error, setError] = useState("invalid password");
    
   
    return(
   
        <Paper className={style.paperBox}>
            <h2 align='center'>Login page</h2>
            <form noValidate autoComplete='off'>
                <TextField  
                    className={style.textField}
                    variant='outlined'
                    placeholder='Masukkan Username'
                    fullWidth />
                <TextField  
                    className={style.textField}
                    variant='outlined'
                    type='password' 
                    placeholder='Password'
                    fullWidth/>
                <Button
                    type='submit'
                    color='secondary'
                    variant='contained'>
                        Login
                </Button>
            </form>
            {error && <p className='error'>{error}</p>}
            
        </Paper>
    )

}
export default Login;
