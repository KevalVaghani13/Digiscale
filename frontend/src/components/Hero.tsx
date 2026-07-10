import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Link } from "wouter";

const blobs = [
  { size: 300, x: "-6%",  y: "10%", duration: 14, delay: 0 },
  { size: 220, x: "78%",  y: "5%",  duration: 18, delay: 2 },
  { size: 160, x: "55%",  y: "55%", duration: 16, delay: 1 },
  { size: 130, x: "18%",  y: "65%", duration: 20, delay: 3 },
];

const dots = Array.from({ length: 20 }, (_, i) => ({
  id: i,
  x: `${(i % 8) * 13 + 2}%`,
  y: `${Math.floor(i / 8) * 34 + 12}%`,
  delay: i * 0.18,
}));

export default function Hero() {
  return (
    <section
      id="home"
      className="relative pt-24 pb-6 lg:pt-28 lg:pb-8 overflow-hidden flex flex-col items-center justify-center min-h-[72vh]"
    >
      {/* Base */}
      <div className="absolute inset-0 -z-10 bg-white" />

      {/* Grid */}
      <div
        className="absolute inset-0 -z-10 opacity-[0.022]"
        style={{
          backgroundImage:
            "linear-gradient(#346BBC 1px, transparent 1px), linear-gradient(90deg, #346BBC 1px, transparent 1px)",
          backgroundSize: "60px 60px",
        }}
      />

      {/* Animated blobs */}
      {blobs.map((b, i) => (
        <motion.div
          key={i}
          className="absolute -z-10 rounded-full bg-primary/5 blur-[80px]"
          style={{ width: b.size, height: b.size, left: b.x, top: b.y }}
          animate={{ y: [0, -20, 0], x: [0, 10, 0] }}
          transition={{ duration: b.duration, delay: b.delay, repeat: Infinity, ease: "easeInOut" }}
        />
      ))}

      {/* Animated dots */}
      {dots.map((d) => (
        <motion.div
          key={d.id}
          className="absolute -z-10 w-1 h-1 rounded-full bg-primary/20"
          style={{ left: d.x, top: d.y }}
          animate={{ opacity: [0.15, 0.6, 0.15], scale: [1, 1.5, 1] }}
          transition={{ duration: 3.2, delay: d.delay, repeat: Infinity, ease: "easeInOut" }}
        />
      ))}

      {/* Top glow */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[360px] -z-10 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-primary/7 via-transparent to-transparent" />

      <div className="container mx-auto px-6 max-w-5xl text-center">
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.45 }}
          className="inline-block mb-4 px-4 py-1.5 rounded-full border border-primary/20 bg-primary/5 text-primary text-sm font-medium"
        >
          AI-Powered Software Development Company
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.45, delay: 0.1 }}
          className="text-4xl md:text-5xl lg:text-[3.75rem] font-extrabold text-foreground tracking-tight leading-[1.1] mb-3"
        >
          Scale Your Business With{" "}
          <br className="hidden md:block" />
          <span className="text-primary">Modern Digital Solutions</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.18 }}
          className="text-sm font-semibold text-primary/60 tracking-[0.2em] mb-4 uppercase"
        >
          Think Digital, Scale Smart
        </motion.p>

        <motion.p
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.24 }}
          className="text-lg md:text-xl text-muted-foreground max-w-[560px] mx-auto mb-7 leading-relaxed"
        >
          We build AI-powered software, modern web applications, and scalable digital solutions for ambitious businesses.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.3 }}
          className="flex flex-col sm:flex-row items-center justify-center gap-3"
        >
          <Button
            asChild
            size="lg"
            className="rounded-full px-8 h-11 text-base bg-primary hover:bg-primary/90 shadow-sm w-full sm:w-auto"
          >
            <Link href="/contact">Book Free Consultation</Link>
          </Button>
          <Button
            asChild
            size="lg"
            variant="outline"
            className="rounded-full px-8 h-11 text-base w-full sm:w-auto hover:bg-primary/5 hover:text-primary border-border"
          >
            <Link href="/case-studies">Explore Work</Link>
          </Button>
        </motion.div>
      </div>
    </section>
  );
}
