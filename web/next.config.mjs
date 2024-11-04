/** @type {import('next').NextConfig} */
const nextConfig = {
  redirects() {
    return [
      {
        source: '/order',
        destination: '/',
        permanent: true,
      },
    ]
  },
};

export default nextConfig;
