import React from 'react'

const Section = (props: {children: JSX.Element[] | JSX.Element}) => {
  return <div className="my-20">{props.children}</div>
}

export default Section
