import Image from "next/image"
import React from "react";

import {InlineMath, BlockMath} from "react-katex"
import 'katex/dist/katex.min.css'

import * as Switch from '@radix-ui/react-switch'
import {Root as Label} from '@radix-ui/react-label'
import * as RadioGroup from '@radix-ui/react-radio-group'

import {useForm, SubmitHandler} from 'react-hook-form'

import gameImage from '../../../images/game-image.jpg'


type ParameterInput = {
  phi: number
  theta: number
}

const GameSection = () => {
  const [qpu, setQpu] = React.useState(false);
  const [phi, setPhi] = React.useState(0);
  const [gamma, setGamma] = React.useState(0);
  const [theta, setTheta] = React.useState(0);
  const [picker, setPicker] = React.useState("simple");


  const {register, handleSubmit, watch} = useForm<ParameterInput>()
  const onSubmit: SubmitHandler<ParameterInput> = data => console.log(data)

  
  const sendRequest = () => {
    fetch(process.env.APIURL || "http://localhost:8080", {
      method: "POST",
      body: JSON.stringify({
        gamma: gamma,
        theta: theta,
        phi: phi,
        qpu: qpu,
      }),
      headers: { "Content-Type": "application/json" },
    });
  };

  return (
    <div className="flex-col w-8/12 space-y-10 mx-auto justify-between">
      <Image
        src={gameImage}
        alt="choices"
      />
      <div className="w-6/12 items-center justify-center">
        <div className="flex">
          <div className="mt-[-0.5] mr-3">
              <InlineMath math="gamma" />
          </div>
          <Label htmlFor="gamma">0</Label>
          <Switch.Root id="gamma" onCheckedChange={() => (gamma === 1 ? setGamma(0) : setGamma(1))}>
            <Switch.SwitchThumb />  
          </Switch.Root>
          <Label htmlFor="gamma" className="ml-3">1</Label>
        </div>
          <BlockMath math="U(\theta,\phi) = \begin{pmatrix} e^{i \phi} cos(\theta/2) &
          sin(\theta/2)\\  -sin(\theta/2) & e^{-i \phi} cos(\theta/2) \end{pmatrix}"/>
      </div>
      <div className="flex-col space-y-5">
        <RadioGroup.Root
          defaultValue="simple"
          onValueChange={(value) => setPicker(value)}
        >
          <div className="flex space-x-5">
            <RadioGroup.Item id="r1" value="simple"><RadioGroup.Indicator /></RadioGroup.Item>
            <Label htmlFor="r1">Simple Picker</Label>
            <RadioGroup.Item id="r2" value="parameter"><RadioGroup.Indicator/></RadioGroup.Item>
            <Label htmlFor="r2">Parameter Picker</Label>
          </div>
        </RadioGroup.Root>
        {picker === "simple" ? (
          <div className="flex space-x-5">
            <button
              onClick={() => {
                setPhi(0);
                setTheta(0);
              }}
            >
              C
            </button>
            <button
              onClick={() => {
                setPhi(0);
                setTheta(1);
              }}
            >
              D
            </button>
            <button
              onClick={() => {
                setPhi(1);
                setTheta(0);
              }}
             >
              Q
            </button>
          </div>
        ) : (
          <form className="flex justify-center items-center space-x-5 w-8/12 mx-auto">
            <div className="flex"> 
              <div className="mt-2 mr-3">
                <InlineMath math="\\phi" />
              </div>
              <input
                defaultValue={0}
                min={0}
                max={1}
                type="number"
              />
            </div>
            <div className="flex">
              <div className="mt-2 mr-3">
                  <InlineMath math="\\theta" />
              </div>
              <input
                defaultValue={0}
                min={0}
                max={1}
                type="number"
              />
             </div>
          </form>
      )}
      </div>
      <button onClick={() => handleSubmit(onSubmit)}>
        Submit
      </button>
    </div>
  );
};

export default GameSection;
