'use client';

import { SectionHeader } from '@/components/home/section-header';
import { siteConfig } from '@/lib/home';
import { cn } from '@/lib/utils';
import { motion } from 'motion/react';
import { ArrowRight } from 'lucide-react';

interface UseCase {
  id: string;
  title: string;
  description: string;
  category: string;
  featured: boolean;
  icon: React.ReactNode;
  image: string;
  url: string;
}

export function UseCasesSection() {
  // Get featured use cases from siteConfig and limit to 8
  const featuredUseCases: UseCase[] = (siteConfig.useCases || []).filter(
    (useCase: UseCase) => useCase.featured,
  );

  return (
    <section
      id="use-cases"
      className="flex flex-col items-center justify-center gap-10 pb-10 w-full relative"
    >
      <SectionHeader>
        <h2 className="text-3xl md:text-4xl font-medium tracking-tighter text-center text-balance">
          See Shukra in action
        </h2>
        <p className="text-muted-foreground text-center text-balance font-medium">
          Explore real-world examples of how Shukra completes complex tasks
          autonomously
        </p>
      </SectionHeader>
    </section>
  );
}
