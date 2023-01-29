import React from 'react'
import {useRouter} from 'next/router'
import Image from 'next/image'
import bgImage from '../../../images/hero-image.jpg'


const HeroSection = () => {
  const router = useRouter()

  return (
    <div className="text-white relative flex h-screen w-full items-center justify-center">
      <div className="flex flex-col space-y-5 justify-center items-center">
        <div className="text-4xl font-semibold">Quantum Prisoner's Dilemma</div>
        <button className="bg-orange-500 text-white h-10 rounded w-64" onClick={() => router.push('/game')}>
          Play the Game
        </button>
      </div>
      <Image
        className="absolute top-0 left-0 z-[-1] h-fit"
        src={bgImage}
        alt="hero-image"
        fill
      />
    </div>
  )
}

export default HeroSection
