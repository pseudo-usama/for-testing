import { LetsGoButton } from "../Components/LetsGoButton"

export const Body = () => {
  return <div className="w-1/3 m-auto mt-20 text-center">
    <div>
      <h1 className="leading-tight text-5xl">Lorem ipsum dolor sit amet consectetur.</h1>
      <p className="mt-5">Lorem ipsum dolor sit amet consectetur adipisicing elit. Possimus deleniti nisi tenetur cum assumenda maxime vero alias ab inventore dicta!</p>
    </div>

    <div className="mt-20 mb-20">
      <LetsGoButton text="lemon pre-sale" />
      <LetsGoButton text="white paper" className="ml-7" />
    </div>
  </div>
}
