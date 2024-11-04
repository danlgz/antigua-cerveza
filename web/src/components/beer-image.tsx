import Cucurucho from "@/app/images/beers/cucurucho.png"
import DonNadie from "@/app/images/beers/don-nadie.png"
import MuyNoble from "@/app/images/beers/muy-noble.png"
import SinNovia from "@/app/images/beers/sin-novia.png"
import Image from "next/image"


type Props = {
  imgName: string
}

export default function BeerImage({ imgName }: Props) {
  let img = Cucurucho;

  if (imgName === "don-nadie") img = DonNadie
  if (imgName === "muy-noble") img = MuyNoble
  if (imgName === "sin-novia") img = SinNovia

  return <Image src={img} alt={imgName} width={50} height={100} />
}
