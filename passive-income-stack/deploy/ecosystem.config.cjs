module.exports = {
  apps: [
    {
      name: 'extract-api',
      cwd: '/root/.openclaw/workspace/passive-income-stack/extract-api',
      script: 'src/index.js',
      interpreter: 'node',
      env: {
        NODE_ENV: 'production',
        PORT: 3001,
        API_KEY: 'CHANGE_ME_EXTRACT_KEY'
      }
    },
    {
      name: 'screenshot-api',
      cwd: '/root/.openclaw/workspace/passive-income-stack/screenshot-api',
      script: 'src/index.js',
      interpreter: 'node',
      env: {
        NODE_ENV: 'production',
        PORT: 3002,
        API_KEY: 'CHANGE_ME_SCREENSHOT_KEY'
      }
    }
  ]
};
