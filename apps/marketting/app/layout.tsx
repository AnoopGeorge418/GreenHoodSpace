import type { Metadata } from 'next';
import { Lora, Geist_Mono, Inter } from 'next/font/google';
import './globals.css';
import { cn } from '@greenhoodspace/ui/lib/utils';

const loraHeading = Lora({ subsets: ['latin'], variable: '--font-heading' });

const inter = Inter({ subsets: ['latin'], variable: '--font-sans' });

const LoraSerif = Lora({ variable: '--font-lora', subsets: ['latin'] });

const geistMono = Geist_Mono({
	variable: '--font-geist-mono',
	subsets: ['latin'],
});

export const metadata: Metadata = {
	title: 'GreenHoodSpace',
	description:
		'GreenHoodSpace is an all-in-one SaaS platform where users can create organizations and institutions, and streamline all their information management in a single, unified workspace.',
};

export default function RootLayout({ children }: LayoutProps<'/'>) {
	return (
		<html
			lang="en"
			className={cn(
				'h-full',
				'antialiased',
				LoraSerif.variable,
				geistMono.variable,
				inter.variable,
				loraHeading.variable,
			)}>
			<body className="min-h-full flex flex-col">{children}</body>
		</html>
	);
}
