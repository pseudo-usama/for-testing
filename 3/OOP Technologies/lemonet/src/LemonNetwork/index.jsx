import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import {
  faArrowLeft,
  faArrowRight
} from "@fortawesome/free-solid-svg-icons"

import './index.scss'

const Box = ({ heading, subHeading, listItems, greenBg }) => {
  const boxClasses = greenBg ? "bg-green-1 text-white" : ""
  const headingClasses = greenBg ? "" : "text-gray-2"
  const subheadingClasses = greenBg ? "" : "text-green-1"
  console.log(listItems)
  return (
    <div className={"py-5 pl-10 pr-20 rounded-lg " + boxClasses}>
      <h1 className={"leading-tight text-4xl font-bold uppercase " + headingClasses}>{heading}</h1>
      <p className={"mt-5 leading-tight text-2xl font-light capitalize " + subheadingClasses}>{subHeading}</p>
      <ul className="list-disc ml-5 mt-3">
        {listItems.map(item => <li key={item}>{item}</li>)}
      </ul>
    </div>
  )
}

export const LemonNetwork = () => {
  return (
    <div className="flex flex-col w-2/3 m-auto items-center lemon-network">
      <h1 className="leading-tight text-4xl font-bold text-green-1 uppercase">Lemon network</h1>
      <p className="w-[650px] mt-5">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Molestias nam velit iure corporis totam quae at ipsa dignissimos dolore accusamus?</p>

      <div className="flex mt-10">
        <Box
          heading="problem"
          subHeading="Lorem ipsum dolor sit."
          listItems={[
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae, magnam.",
            "Lorem ipsum dolor sit amet.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis, rerum!"
          ]}
        />
        <Box
          heading="solution"
          subHeading="Lorem ipsum dolor sit."
          listItems={[
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Vitae, magnam.",
            "Lorem ipsum dolor sit amet.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis, rerum!"
          ]}
          greenBg
        />
      </div>
      <div className="ml-auto mt-3">
        <FontAwesomeIcon className="text-[15px] text-gray-3 cursor-pointer" icon={faArrowLeft} />
        <FontAwesomeIcon className="text-[15px] text-gray-3 cursor-pointer ml-3" icon={faArrowRight} />
      </div>
    </div>
  )
}
