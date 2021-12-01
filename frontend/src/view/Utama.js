import React from 'react';

const Utama = props =>{
    return(
        <>
        <div className="flex justify-center">
            <img className = 'img order-2 mt-5' src="Frame 2.png" width="500" height="600"></img>
            <div className="order-1 flex flex-col p-16">
                <div className="text-5xl font-semibold mt-16 ml-16">Promosikan produk dan dapatkan fee-nya!</div>
                <div className="sm extralight text-left	text-gray-500 mt-20 ml-16">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s,</div>
                <div className="grid-col-2 mx-32 my-10"> 
                    <button class="bg-purple-800 shadow-xl	rounded-lg">SAYA PEMILIK BRAND</button>
                    <button class="bg-purple-800 shadow-xl	rounded-lg ml-16">SAYA INFLUENCER</button>
                </div>
            </div>
        </div>
        
        
    
        </>
    );
}

export default Utama;