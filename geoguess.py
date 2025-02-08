from discord.ext import commands
from bot.utils.cloudflare import enumerate_caches
from bot.utils.geolocation import estimate_location

class Geoguess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="geoguess")
    async def geoguess(self, ctx, username: str):
        await ctx.send(f"Running geoguess attack on {username}...")

        # Step 1: Trigger a cache hit (simulated)
        resource_url = "https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}"
        caches = enumerate_caches(resource_url)

        # Step 2: Estimate location
        location = estimate_location(caches)

        # Step 3: Generate map URL
        map_url = f"http://localhost:5000/map?lat={location['lat']}&lng={location['lng']}"
        await ctx.send(f"Estimated location for {username}: {map_url}")

async def setup(bot):
    await bot.add_cog(Geoguess(bot))