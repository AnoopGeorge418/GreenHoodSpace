import type { NextConfig } from "next";

const nextConfig: NextConfig = {
    /* config options here */
    transpilePackages: ["@greenhoodspace/ui"],
    reactCompiler: true,
};

export default nextConfig;
