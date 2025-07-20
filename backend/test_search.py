#!/usr/bin/env python3
"""
Test script to diagnose search functionality issues.
Run this script to check if the search APIs are properly configured and working.
"""

import asyncio
import os
import sys
from dotenv import load_dotenv

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables first
load_dotenv()

# Check for required environment variables before importing config
def check_env_vars():
    """Check if required environment variables are set"""
    print("🔍 Checking Environment Variables...")
    
    required_vars = {
        'TAVILY_API_KEY': 'Tavily API key for web search',
        'FIRECRAWL_API_KEY': 'Firecrawl API key for web scraping'
    }
    
    missing_vars = []
    for var, description in required_vars.items():
        if not os.getenv(var):
            missing_vars.append(f"{var} ({description})")
        else:
            print(f"✅ {var}: {os.getenv(var)[:10]}...")
    
    if missing_vars:
        print("\n❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 Please create a .env file with these variables:")
        print("   TAVILY_API_KEY=your_tavily_api_key")
        print("   FIRECRAWL_API_KEY=your_firecrawl_api_key")
        return False
    
    print("✅ All required environment variables are set")
    return True

async def test_tavily_direct():
    """Test Tavily API directly without using the config module"""
    print("\n🔍 Testing Tavily API...")
    
    tavily_key = os.getenv('TAVILY_API_KEY')
    if not tavily_key:
        print("❌ TAVILY_API_KEY not found in environment")
        return False
    
    try:
        from tavily import AsyncTavilyClient
        
        client = AsyncTavilyClient(api_key=tavily_key)
        print("✅ Tavily client created successfully")
        
        # Test a simple search
        print("🔍 Testing search functionality...")
        result = await asyncio.wait_for(
            client.search(
                query="test query",
                max_results=1,
                include_images=False,
                include_answer=False,
                search_depth="basic",
            ),
            timeout=30.0
        )
        
        if result and 'results' in result:
            print(f"✅ Search test successful! Found {len(result.get('results', []))} results")
            return True
        else:
            print("❌ Search returned unexpected response format")
            return False
            
    except asyncio.TimeoutError:
        print("❌ Search request timed out")
        return False
    except Exception as e:
        print(f"❌ Search test failed: {str(e)}")
        return False

async def test_firecrawl_direct():
    """Test Firecrawl API directly"""
    print("\n🌐 Testing Firecrawl API...")
    
    firecrawl_key = os.getenv('FIRECRAWL_API_KEY')
    if not firecrawl_key:
        print("❌ FIRECRAWL_API_KEY not found in environment")
        return False
    
    try:
        import httpx
        
        async with httpx.AsyncClient() as client:
            headers = {
                "Authorization": f"Bearer {firecrawl_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "url": "https://example.com",
                "formats": ["markdown"]
            }
            
            firecrawl_url = os.getenv('FIRECRAWL_URL', 'https://api.firecrawl.dev')
            
            response = await asyncio.wait_for(
                client.post(
                    f"{firecrawl_url}/v1/scrape",
                    json=payload,
                    headers=headers,
                ),
                timeout=30.0
            )
            
            if response.status_code == 200:
                print("✅ Firecrawl API test successful!")
                return True
            else:
                print(f"❌ Firecrawl API returned status {response.status_code}: {response.text}")
                return False
                
    except asyncio.TimeoutError:
        print("❌ Firecrawl request timed out")
        return False
    except Exception as e:
        print(f"❌ Firecrawl test failed: {str(e)}")
        return False

async def test_network_connectivity():
    """Test basic network connectivity"""
    print("\n🌐 Testing Network Connectivity...")
    
    try:
        import httpx
        
        async with httpx.AsyncClient() as client:
            # Test basic internet connectivity
            response = await asyncio.wait_for(
                client.get("https://httpbin.org/get"),
                timeout=10.0
            )
            
            if response.status_code == 200:
                print("✅ Basic internet connectivity working")
                return True
            else:
                print(f"❌ Internet connectivity test failed: {response.status_code}")
                return False
                
    except Exception as e:
        print(f"❌ Network connectivity test failed: {str(e)}")
        return False

async def main():
    """Run all tests"""
    print("🚀 Starting Search Configuration Tests...\n")
    
    # Check environment variables first
    env_ok = check_env_vars()
    
    if not env_ok:
        print("\n⚠️  Please configure your environment variables before running tests.")
        print("   Copy .env.example to .env and add your API keys:")
        print("   cp .env.example .env")
        print("   # Then edit .env and add your API keys")
        return
    
    # Test network connectivity first
    network_ok = await test_network_connectivity()
    
    # Test API configurations
    tavily_ok = await test_tavily_direct()
    firecrawl_ok = await test_firecrawl_direct()
    
    # Summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)
    
    if network_ok:
        print("✅ Network connectivity: OK")
    else:
        print("❌ Network connectivity: FAILED")
    
    if tavily_ok:
        print("✅ Tavily API: OK")
    else:
        print("❌ Tavily API: FAILED")
    
    if firecrawl_ok:
        print("✅ Firecrawl API: OK")
    else:
        print("❌ Firecrawl API: FAILED")
    
    if network_ok and tavily_ok and firecrawl_ok:
        print("\n🎉 All tests passed! Search functionality should work correctly.")
    else:
        print("\n⚠️  Some tests failed. Please check the configuration and try again.")
        print("\n📝 Common solutions:")
        print("   1. Ensure all API keys are properly configured in .env file")
        print("   2. Check your internet connection")
        print("   3. Verify API key validity and quotas")
        print("   4. Check if the APIs are experiencing downtime")

if __name__ == "__main__":
    asyncio.run(main()) 