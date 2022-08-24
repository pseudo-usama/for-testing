import { Navbar } from "./Navbar"
import { Body } from "./Body"
import { SocialSidebar } from "./SocialSidebar"

import "./index.scss"

export const Header = () => {
  return (
    <div className="bg-gradient-to-br from-yellow-1 to-green-1">
      <div className="relative pb-[250px] text-white header">
        <Navbar />
        <Body />
        <SocialSidebar />
      </div>
      <div className="relative mt-0">
        <div className="absolute curved-div"></div>
        <div className="absolute curved-div"></div>
        <div className="absolute curved-div"></div>
      </div>
    </div>
  )
}
