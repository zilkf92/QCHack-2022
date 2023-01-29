import Link from 'next/link'
import React from 'react'

const Navbar = () => {
  return (
    <div className="text-white flex h-16 w-full items-center justify-between bg-slate-800 px-20">
      <Link className="text-2xl" href="/">
        Quantum Prisoner's Dilemma
      </Link>
      <div className="flex w-1/12 text-xl space-x-4">
        <Link href="/tutorial">Tutorial</Link>
        <Link href="/game">Game</Link>
      </div>
    </div>
  )
}

export default Navbar
