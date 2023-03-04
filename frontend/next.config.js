/* eslint-disable */
/** @type {import('next').NextConfig} */
const nextConfig = {
    webpack: (config, { dev, isServer }) => {
        if (dev && !isServer) {
            config.watchOptions = {
                poll: 1000,
                aggregateTimeout: 300,
            };
        }
        return config;
    },
    reactStrictMode: true,
};

module.exports = nextConfig;
