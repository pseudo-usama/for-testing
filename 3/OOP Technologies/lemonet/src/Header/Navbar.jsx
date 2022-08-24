import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faDharmachakra, faAngleDown } from "@fortawesome/free-solid-svg-icons"
import { Button } from "../Components/Button"

const LangMenu = () => {
  return <div className="group">
    <button className="px-7 py-3 rounded-tl rounded-tr group-hover:bg-white group-hover:text-green-1">
      English
      <FontAwesomeIcon className="ml-3 group-hover:rotate-180" icon={faAngleDown} />
    </button>
    <ul className="hidden absolute bg-white rounded-bl rounded-br text-green-1 group-hover:block">
      <li className="px-10 py-3"><a href="#">English</a></li>
      <li className="px-10 py-3"><a href="#">Urdu</a></li>
    </ul>
  </div>
}

const LeftMenu = () => {
  return <div className="ml-10">
    <ul className="flex gap-8">
      <li><a href="#">About</a></li>
      <li><a href="#">Why</a></li>
      <li><a href="#">Benefit</a></li>
      <li><a href="#">Token Sale</a></li>
      <li><a href="#">Roadmap</a></li>
      <li><a href="#">FAQ</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </div>
}

const RightMenu = () => {
  return <div className="ml-auto flex items-center">
    <LangMenu />

    <div>
      <Button text={"Connect Wallet"} />
      <Button text={"PRE-SALE"} noBg />
    </div>
  </div>
}

export const Navbar = () => {
  return <div className="flex items-center px-5 pt-5">
    <a href="#">
      <h1 className="leading-tight text-4xl ml-2 text-600 uppercase">
        <FontAwesomeIcon className="text-[40px] mr-4" icon={faDharmachakra} />
        lemonet
      </h1>
    </a>

    <LeftMenu />
    <RightMenu />
  </div>
}
