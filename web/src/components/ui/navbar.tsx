import Image, { StaticImageData } from "next/image";
import Link from "next/link";

type Props = {
  lightLogo: StaticImageData,
  darkLogo: StaticImageData,
}

export default function Navbar({ lightLogo, darkLogo }: Props) {
  return (
    <header className="flex justify-center border-b py-4 shadow-sm sticky top-0 bg-background z-10">
      <Link href="/">
        <Image src={darkLogo} className="hidden dark:block" alt="Antigua Cerveza logo" width={200} height={50} />
        <Image src={lightLogo} className="block dark:hidden" alt="Antigua Cerveza logo" width={200} height={50} />
      </Link>
    </header>
  )
}
