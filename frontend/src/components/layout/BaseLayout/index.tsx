import React from 'react'

import Navbar from '../../molecules/Navbar'
import Footer from '../../molecules/Footer'

const BaseLayout = (props: {children: JSX.Element[] | JSX.Element}) => {
  return (
    <div className="flex-col items-center justify-center">
      <Navbar />
      {props.children}
      <Footer />
    </div>
  )
}

export default BaseLayout
