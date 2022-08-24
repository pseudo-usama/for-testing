import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import {
  faFacebookF,
  faTwitter,
  faYoutube,
  faGithub,
  faRedditAlien,
} from "@fortawesome/free-brands-svg-icons"

export const SocialSidebar = () => {
  return <div className="absolute right-5 top-[50%] -translate-y-2/4">
    <ul className="inline-flex flex-col items-center gap-4 p-4 rounded-full bg-gray-1">
      <li><a href="#"><FontAwesomeIcon className="text-[15px]" icon={faFacebookF} /></a></li>
      <li><a href="#"><FontAwesomeIcon className="text-[15px]" icon={faTwitter} /></a></li>
      <li><a href="#"><FontAwesomeIcon className="text-[15px]" icon={faYoutube} /></a></li>
      <li><a href="#"><FontAwesomeIcon className="text-[15px]" icon={faGithub} /></a></li>
      <li><a href="#"><FontAwesomeIcon className="text-[15px]" icon={faRedditAlien} /></a></li>
    </ul>
  </div>
}