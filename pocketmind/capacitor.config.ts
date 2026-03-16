import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.pocketpal.app',
  appName: 'PocketPal',
  webDir: 'build',
  server: {
    // Change this to your PocketPal server URL
    // Local: http://<your-computer-ip>:5005
    // Production: https://your-server.com
    url: 'http://localhost:5005',
    androidScheme: 'http'
  },
  plugins: {
    SplashScreen: {
      launchShowDuration: 2000,
      backgroundColor: '#161b22'
    }
  }
};

export default config;
