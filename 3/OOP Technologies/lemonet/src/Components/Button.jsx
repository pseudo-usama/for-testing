export const Button = ({ text, noBg, onClick, className }) => {
  const bgOrBorder = noBg ? "border-solid border-2 border-light-white-3 hover:bg-light-white-3" : "bg-light-white-3 hover:bg-light-white-4"

  return <>
    <button
      className={`px-7 py-3 ml-5 rounded-full ${bgOrBorder} ${className}`}
      onClick={onClick}
    >
      {text}
    </button>
  </>
}
