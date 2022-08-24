import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faAnglesRight } from "@fortawesome/free-solid-svg-icons"

export const LetsGoButton = ({ text, onClick, className }) => {
  return <>
    <button
      className={"inline-flex items-center group pl-5 bg-white text-green-1 uppercase rounded-full text-center " + className}
      onClick={onClick}
    >
      {text}
      <FontAwesomeIcon
        className="text-[15px] ml-5 m-1 px-3.5 py-3 text-white bg-green-1 rounded-full duration-200 group-hover:translate-x-[2px]"
        icon={faAnglesRight}
      />
    </button>
  </>
}
