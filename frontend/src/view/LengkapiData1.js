import { Button, makeStyles, Paper, Typography, TextField } from "@material-ui/core";
import { Stack } from "@mui/material";
import React from "react";
import { ReactComponent as LogoBack} from '../Asset/LogoBack.svg'

const useStyles = makeStyles((theme) => ({
    root:{
        display: 'flex',
        flexWrap: 'wrap',
    },
    paperBox:{
        elevation: 30,
        padding: 20,
        display: 'flex',
        flexDirection:"column",
        flexWrap: 'wrap',
        height:'800px', 
        width:'700px',
        margin:'10px auto',
        backgroundColor: '#ffffff',
    },
    buttonBack:{
        margin:'30px auto',
        display: 'flex',
        width:'700px',
        height: 60,
        alignContent: 'flex-start',
        elevation: 10,
        backgroundColor: '#ffffff',
    }

}))



export default function LengkapiData(){
    const style = useStyles();
    
    return(
        <><Button className={style.buttonBack}
            variant='contained'
            startIcon={<LogoBack
                style={{ height: 53, width: 36 }} />}
        >Data profil
        </Button>
        <Paper className={style.paperBox}
            variant='outlined'>
                 <form noValidate autoComplete='off'>
                     <Stack direction='column' spacing={1} style={{margin: '10px auto'}}>
                         <Typography variant='body1'  component="div" gutterBottom>
                             Nama Lengkap (sesuai kartu identitas)
                         </Typography>
                         <TextField  
                            className={style.textField}
                            variant='outlined'
                            id='fullname'
                            placeholder='Nama lengkap'
                            fullWidth
                            />
                        <Typography variant='body1'  component="div" gutterBottom>
                             Tanggal lahir
                         </Typography>
                         <TextField  
                            className={style.textField}
                            id='date'
                            type='date'/>
                        <Typography variant='body1'  component="div" gutterBottom>
                             Kota
                         </Typography>
                         <TextField  
                            className={style.textField}
                            variant='outlined'
                            id='fullname'
                            placeholder='Kota'
                            fullWidth
                            />
                        <Typography variant='body1'  component="div" gutterBottom>
                             Nomor telepon
                         </Typography>
                         <TextField  
                            className={style.textField}
                            variant='outlined'
                            id='fullname'
                            placeholder='Nomor telepon'
                            fullWidth
                            />
                     </Stack>
                 </form>
            </Paper></>
    )
}