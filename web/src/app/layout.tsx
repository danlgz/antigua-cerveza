import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Navbar from "@/components/ui/navbar";
import LightLogo from "@/app/images/antigua-cerveza-logo.png"
import DarkLogo from "@/app/images/antigua-cerveza-logo-dark.png"


const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Antigua Cerveza",
  description: "Visualizador de ordenes",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased relative`}
      >
        <Navbar lightLogo={LightLogo} darkLogo={DarkLogo} />
        <main className="max-w-screen-lg mx-auto p-4 my-4">
          {children}
        </main>
      </body>
    </html>
  );
}
