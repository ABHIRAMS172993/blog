import React from 'react'

const Header = () => {
  return (
    <div className='bg-blue-300 p-2'>
        <img src="https://imgs.search.brave.com/k35Tgw9jo9MLTssNS3sMlbL3AafnES6lRIL9-29Hx2w/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzE5LzIyLzc3LzM1/LzM2MF9GXzE5MjI3/NzM1MjdfY3pOR3o5/T3NWUXhmNjFoT3FD/b3k3b0U4bW9xU1Zu/SDcuanBn" alt="" className='w-8 h-8 bg-none'/>
       <div className='flex justify-end gap-2'>
            <a href="">Home</a>
            <a href="">Contact</a>
            <a href=""></a>
       </div>
    </div>

  )
}

export default Header