const Digit = ({ number, letter, noColon }) => {
  return (
    <div className="flex font-bold">
      <div className="flex flex-col items-center">
        <span className="text-2xl text-yellow-1 italic">{number}</span>
        <span className="-mt-2 font-normal text-sm">{letter}</span>
      </div>
      {!noColon && <span className="ml-3 text-2xl text-yellow-1 italic">:</span>}
    </div>
  )
}

const Timer = () => {
  return <div className="px-10 py-8 bg-white rounded-tl-lg rounded-bl-lg shadow-2xl">
    <p className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-green-1 to-yellow-1">
      Pre-sale is live now
    </p>
    <div className="mt-3">
      <p>Pre-sale end in</p>
      <div className="flex gap-2">
        <Digit number={12} letter="D" />
        <Digit number={12} letter="H" />
        <Digit number={12} letter="M" />
        <Digit number={12} letter="S" noColon />
      </div>
    </div>
  </div>
}

const ProgressBar = () => {
  return <div className="px-10 py-8 w-[500px] bg-green-2 text-white rounded-tr-lg rounded-br-lg shadow-2xl">
    <p>Pre sale</p>
    <div className="w-full h-6 mt-3 p-1 bg-gray-200 rounded-full">
      <div className="w-[35%] h-4 rounded-full bg-gradient-to-br from-yellow-1 to-green-1"></div>
    </div>
    <div className="flex justify-between">
      <p>Softcap reached</p>
      <p>123,456 Sold</p>
    </div>
  </div>
}

export const PreSale = () => {
  return (
    <div className="flex justify-center -translate-y-full">
      <Timer />
      <ProgressBar />
    </div>
  )
}
