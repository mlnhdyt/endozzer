import React from 'react';
import {IconButton, AppBar, makeStyles, Toolbar, Button, styled, Typography, Grid } from '@material-ui/core';
import { purple } from '@material-ui/core/colors';

const ColorButton = styled(Button)(({ theme }) => ({
    color: theme.palette.getContrastText(purple[500]),
    backgroundColor: purple[500],
    '&:hover': {
      backgroundColor: purple[700],
    },
  }));
  
const Utama = props =>{
    return(
        <>
        <div className="flex justify-center">
            <img className = 'img order-2 mt-5' src="Frame 2.png" width="500" height="600"></img>
            <div className="order-1 flex flex-col p-16 mx-24 my-24">
                <div className="text-5xl font-semibold">Promosikan produk dan dapatkan fee-nya!</div>
                <div className="text-left text-gray-400 mt-16">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s,</div>
                <div className="grid-rows-2 mt-8 ml-16"> 
                    <ColorButton className="text-2xl font-light" variant="contained">SAYA PEMILIK BRAND</ColorButton>
                    <ColorButton className="text-2xl font-light" variant="contained">SAYA INFLUENCER</ColorButton>
                </div>
            </div>
        </div>

        <div className="flex justify-center mx-40 my-40">
            <img className = 'img order-1' src="Frame 3.png" width="300" height="50"></img>
            <div className="order-2 flex flex-col">
                <div className="text-3xl font-medium pl-8 text-purple-700">Apakah Itu ENDOZZER?</div>
                <div className="text-justify pl-8 pt-8 text-gray-400">ENDOZZER merupakan platform influencer marketing yang menyediakan fasilitas bagi brand-owner untuk menemukan influencer dalam mempromosikan produk mereka. Brand-owner dapat menemukan influencer yang tepat sesuai kriteria yang diinginkan dan Influencer bisa mendapatkan uang saku tambahan hanya dengan memposting campaign dari sebuah perusahaan.</div>
            </div>
        </div>

        <div className="flex-col mx-40 my-40">
            <div className="flex justify-center text-3xl font-medium pl-8 text-purple-700">HOW IT WORKS</div>
            <div className="flex flex-col">
                <div className="flex flex-row">
                    <img className='img' src="Rectangle 223.png" width="500" height="50"></img>
                    <img className='img' src="Rectangle 225.png" width="500" height="50"></img>
                </div>
                
                <div className="flex flex-row">
                    <div className="text-2xl font-light text-left">Untuk Pemilik Brand</div>
                    <div className="text-2xl font-light text-left">Untuk Influencer</div>
                </div>

                <div className="flex flex-row">
                    <div className="font-light text-left text-gray-400">Platform ENDOZZER membantu small business dalam menemukan influencer yang tepat untuk mempromosikan produknya.</div>
                    <div className="font-light text-left text-gray-400">Jadikan Media Sosial kamu tempat untukmu berkreasi dan menghasilkan pendapatan.</div>
                </div>
            </div>
        </div>
        </>
    );
}

export default Utama;