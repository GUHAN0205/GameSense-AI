# Deployment Guide

This guide covers deploying both the frontend and backend of the AI Game Coach application.

## Frontend Deployment

### Option 1: Vercel (Recommended)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Build the project**
   ```bash
   npm run build
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Set Environment Variables**
   - Go to your Vercel project settings
   - Add `VITE_API_URL` with your backend URL

### Option 2: Netlify

1. **Build the project**
   ```bash
   npm run build
   ```

2. **Deploy via Netlify CLI**
   ```bash
   npm install -g netlify-cli
   netlify deploy --prod --dir=dist
   ```

3. **Set Environment Variables**
   - In Netlify dashboard: Site settings → Environment variables
   - Add `VITE_API_URL` with your backend URL

### Option 3: GitHub Pages

1. **Install gh-pages**
   ```bash
   npm install --save-dev gh-pages
   ```

2. **Update package.json**
   ```json
   {
     "scripts": {
       "deploy": "npm run build && gh-pages -d dist"
     }
   }
   ```

3. **Deploy**
   ```bash
   npm run deploy
   ```

## Backend Deployment

### Option 1: Heroku

1. **Create `requirements.txt`**
   ```
   Flask==2.3.0
   flask-cors==4.0.0
   gunicorn==21.2.0
   ```

2. **Create `Procfile`**
   ```
   web: gunicorn backend_enhanced:app
   ```

3. **Deploy**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Option 2: Railway

1. **Create `requirements.txt`** (same as above)

2. **Create `railway.json`**
   ```json
   {
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "gunicorn backend_enhanced:app",
       "restartPolicyType": "ON_FAILURE"
     }
   }
   ```

3. **Deploy via Railway CLI or GitHub integration**

### Option 3: Render

1. **Create `requirements.txt`** (same as above)

2. **Create `render.yaml`**
   ```yaml
   services:
     - type: web
       name: ai-game-coach
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: gunicorn backend_enhanced:app
       envVars:
         - key: PORT
           value: 10000
   ```

3. **Deploy via Render dashboard or GitHub**

### Option 4: DigitalOcean App Platform

1. **Prepare files** (requirements.txt)

2. **Deploy via UI**
   - Connect GitHub repository
   - Select Python environment
   - Set start command: `gunicorn backend_enhanced:app`

## Environment Variables

### Frontend
- `VITE_API_URL` - Backend API URL (e.g., https://api.yourdomain.com)

### Backend
- `PORT` - Server port (usually set by hosting platform)
- `DEBUG` - Set to "false" in production
- `FLASK_ENV` - Set to "production"

## Post-Deployment Checklist

- [ ] Verify frontend can connect to backend
- [ ] Test all API endpoints
- [ ] Check CORS configuration
- [ ] Verify SSL/HTTPS is enabled
- [ ] Test on different devices and browsers
- [ ] Monitor error logs
- [ ] Set up analytics (optional)
- [ ] Configure custom domain (optional)

## Troubleshooting

### CORS Errors
- Ensure backend CORS is configured with frontend URL
- Check that both frontend and backend use HTTPS

### API Connection Failed
- Verify `VITE_API_URL` is correct
- Check backend is running and accessible
- Review network requests in browser DevTools

### Build Failures
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Clear build cache: `rm -rf dist`
- Check Node.js version compatibility

## Performance Optimization

1. **Enable Compression**
   - Most hosting platforms enable this by default

2. **CDN Setup**
   - Use Cloudflare or similar for static assets

3. **Caching**
   - Configure proper cache headers for static files

4. **Monitoring**
   - Set up error tracking (Sentry, LogRocket)
   - Monitor API response times

## Security Considerations

1. **API Rate Limiting**
   - Implement rate limiting on backend
   - Use Flask-Limiter or similar

2. **Input Validation**
   - Already implemented in backend_enhanced.py

3. **HTTPS**
   - Ensure both frontend and backend use HTTPS

4. **API Keys**
   - Never commit API keys to version control
   - Use environment variables

## Scaling

### Frontend
- Static hosting scales automatically
- Use CDN for global distribution

### Backend
- Add more server instances via platform
- Implement caching (Redis)
- Use database for persistent storage
- Add load balancer for high traffic

## Monitoring & Analytics

### Recommended Tools
- **Frontend**: Google Analytics, Vercel Analytics
- **Backend**: Application Performance Monitoring (APM)
- **Errors**: Sentry, Rollbar
- **Uptime**: UptimeRobot, Pingdom

## Cost Estimates

### Frontend (Static Hosting)
- Vercel: Free tier available
- Netlify: Free tier available
- GitHub Pages: Free

### Backend
- Heroku: $7/month (Hobby tier)
- Railway: $5/month (Developer tier)
- Render: Free tier available
- DigitalOcean: $5/month (Basic Droplet)

---

For questions or issues, refer to the main README.md or open an issue.
