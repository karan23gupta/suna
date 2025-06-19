import Image from 'next/image';
import { siteConfig } from '@/lib/home';
import Link from 'next/link';

export function CTASection() {
  const { ctaSection } = siteConfig;

  return (
    <section
      id="cta"
      className="flex flex-col items-center justify-center w-full pt-12 pb-12"
    >
      <div className="w-full max-w-6xl mx-auto px-6">
        <div className="h-[400px] md:h-[400px] overflow-hidden shadow-xl w-full border border-border rounded-xl bg-secondary relative z-20">
          {/* <Image
            src={ctaSection.backgroundImage}
            alt="Agent CTA Background"
            className="absolute inset-0 w-full h-full object-cover object-right md:object-center"
            fill
            priority
          /> */}
          <div className="absolute inset-0 -top-32 md:-top-40 flex flex-col items-center justify-center">
            <div className="flex flex-col items-center gap-4">
              <span className="text-white/80 text-sm font-medium bg-white/10 px-3 py-1 rounded-full">
                Currently in Closed Beta
              </span>
              <h1 className="text-white text-4xl md:text-7xl font-medium tracking-tighter max-w-xs md:max-w-xl text-center">
                {ctaSection.title}
              </h1>
            </div>
            <div className="absolute bottom-10 flex flex-col items-center justify-center gap-2">
              <Link
                href={ctaSection.button.href}
                className="bg-white text-black font-semibold text-sm h-10 w-fit px-4 rounded-full flex items-center justify-center shadow-md"
              >
                Request Early Access
              </Link>
              <span className="text-white text-sm">Limited spots available</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
