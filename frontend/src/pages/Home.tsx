import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import TrustedBy from "@/components/TrustedBy";
import Services from "@/components/Services";
import Portfolio from "@/components/Portfolio";
import Process from "@/components/Process";
import TechStack from "@/components/TechStack";
import Testimonials from "@/components/Testimonials";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main className="min-h-screen w-full flex flex-col bg-background">
      <Navbar />
      <Hero />
      <TrustedBy />
      <Services />
      <Portfolio />
      <Process />
      <TechStack />
      <Testimonials />
      <Contact />
      <Footer />
    </main>
  );
}