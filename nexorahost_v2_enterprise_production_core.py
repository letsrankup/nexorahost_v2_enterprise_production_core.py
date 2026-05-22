'use client'

import { useState } from 'react'

export default function NexoraHost() {
  const [domain, setDomain] = useState('')
  const [result, setResult] = useState('')

  const affiliateLink =
    'https://hostinger.com?REFERRALCODE=YOURCODE'

  const checkDomain = async () => {
    if (!domain) return

    setResult(`"${domain}" looks available!`)
  }

  const plans = [
    {
      name: 'Premium Hosting',
      price: '$2.99/mo',
      features: [
        'Free SSL',
        'Free Domain',
        '100 Websites',
        'LiteSpeed Servers',
      ],
    },
    {
      name: 'Business Hosting',
      price: '$5.99/mo',
      features: [
        'Daily Backups',
        'Cloudflare CDN',
        'AI Tools',
        'Priority Support',
      ],
    },
    {
      name: 'Cloud Startup',
      price: '$9.99/mo',
      features: [
        'Dedicated Resources',
        'Advanced Security',
        'Unlimited Bandwidth',
        'Free Migration',
      ],
    },
  ]

  return (
    <main className="min-h-screen bg-black text-white">
      {/* NAVBAR */}
      <nav className="flex items-center justify-between px-8 py-6 border-b border-zinc-800">
        <h1 className="text-3xl font-bold text-purple-500">
          NexoraHost
        </h1>

        <div className="flex gap-6 text-sm">
          <a href="#plans">Hosting</a>
          <a href="#domain">Domains</a>
          <a href="#reviews">Reviews</a>
          <a href="#blog">Blog</a>
        </div>
      </nav>

      {/* HERO */}
      <section className="text-center py-28 px-6 bg-gradient-to-b from-purple-950 to-black">
        <h2 className="text-6xl font-bold leading-tight mb-6">
          Best Hosting Deals <br />
          For Your Website
        </h2>

        <p className="text-zinc-400 text-lg max-w-2xl mx-auto mb-10">
          Compare premium hosting providers and launch your
          website with ultra-fast cloud hosting.
        </p>

        <div className="flex justify-center gap-5 flex-wrap">
          <a
            href={affiliateLink}
            target="_blank"
            className="bg-purple-600 hover:bg-purple-500 px-8 py-4 rounded-2xl text-lg font-bold"
          >
            Get Hosting
          </a>

          <a
            href="#plans"
            className="border border-zinc-700 px-8 py-4 rounded-2xl"
          >
            Compare Plans
          </a>
        </div>
      </section>

      {/* DOMAIN SEARCH */}
      <section
        id="domain"
        className="max-w-5xl mx-auto px-6 py-24"
      >
        <div className="bg-zinc-900 border border-zinc-800 rounded-3xl p-10">
          <h2 className="text-4xl font-bold mb-6 text-center">
            Search Your Domain
          </h2>

          <div className="flex flex-col md:flex-row gap-4">
            <input
              value={domain}
              onChange={(e) => setDomain(e.target.value)}
              placeholder="Enter domain name..."
              className="flex-1 bg-black border border-zinc-700 p-4 rounded-2xl"
            />

            <button
              onClick={checkDomain}
              className="bg-purple-600 hover:bg-purple-500 px-8 rounded-2xl font-bold"
            >
              Search
            </button>
          </div>

          {result && (
            <div className="mt-6 text-green-400 text-center">
              {result}
            </div>
          )}

          <div className="text-center mt-8">
            <a
              href={affiliateLink}
              target="_blank"
              className="inline-block bg-white text-black px-8 py-4 rounded-2xl font-bold"
            >
              Buy Domain & Hosting
            </a>
          </div>
        </div>
      </section>

      {/* HOSTING PLANS */}
      <section
        id="plans"
        className="max-w-7xl mx-auto px-6 py-20"
      >
        <div className="text-center mb-16">
          <h2 className="text-5xl font-bold mb-4">
            Hosting Plans
          </h2>

          <p className="text-zinc-400">
            Professional hosting packages for all websites.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {plans.map((plan, i) => (
            <div
              key={i}
              className="bg-zinc-900 border border-zinc-800 rounded-3xl p-8 hover:border-purple-500 transition"
            >
              <h3 className="text-3xl font-bold mb-4">
                {plan.name}
              </h3>

              <p className="text-5xl font-bold text-purple-400 mb-8">
                {plan.price}
              </p>

              <ul className="space-y-4 mb-10 text-zinc-300">
                {plan.features.map((f, idx) => (
                  <li key={idx}>✓ {f}</li>
                ))}
              </ul>

              <a
                href={affiliateLink}
                target="_blank"
                className="block text-center bg-purple-600 hover:bg-purple-500 py-4 rounded-2xl font-bold"
              >
                Buy Hosting
              </a>
            </div>
          ))}
        </div>
      </section>

      {/* REVIEWS */}
      <section
        id="reviews"
        className="bg-zinc-950 py-24 px-6"
      >
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-5xl font-bold mb-4">
              Why Choose Us
            </h2>

            <p className="text-zinc-400">
              Trusted hosting recommendations for creators,
              bloggers, and businesses.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-black border border-zinc-800 rounded-3xl p-8">
              <h3 className="text-2xl font-bold mb-4">
                Fast Servers
              </h3>

              <p className="text-zinc-400">
                Optimized cloud infrastructure for ultra-fast
                loading speeds.
              </p>
            </div>

            <div className="bg-black border border-zinc-800 rounded-3xl p-8">
              <h3 className="text-2xl font-bold mb-4">
                Free SSL
              </h3>

              <p className="text-zinc-400">
                Secure your website with free SSL certificates.
              </p>
            </div>

            <div className="bg-black border border-zinc-800 rounded-3xl p-8">
              <h3 className="text-2xl font-bold mb-4">
                AI Website Tools
              </h3>

              <p className="text-zinc-400">
                Build websites quickly using AI-powered tools.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* BLOG */}
      <section
        id="blog"
        className="max-w-7xl mx-auto py-24 px-6"
      >
        <div className="text-center mb-16">
          <h2 className="text-5xl font-bold mb-4">
            Latest Guides
          </h2>

          <p className="text-zinc-400">
            Learn how to build and grow websites online.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[1, 2, 3].map((item) => (
            <div
              key={item}
              className="bg-zinc-900 border border-zinc-800 rounded-3xl overflow-hidden"
            >
              <div className="h-48 bg-gradient-to-r from-purple-700 to-indigo-700"></div>

              <div className="p-8">
                <h3 className="text-2xl font-bold mb-4">
                  How To Start A Website In 2026
                </h3>

                <p className="text-zinc-400 mb-6">
                  Complete guide for beginners to launch a
                  website online.
                </p>

                <a
                  href={affiliateLink}
                  target="_blank"
                  className="text-purple-400 font-bold"
                >
                  Read More →
                </a>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section className="py-24 px-6">
        <div className="max-w-5xl mx-auto bg-gradient-to-r from-purple-700 to-indigo-700 rounded-3xl p-16 text-center">
          <h2 className="text-5xl font-bold mb-6">
            Launch Your Website Today
          </h2>

          <p className="text-lg mb-10 text-zinc-100">
            Start your online journey with premium cloud hosting.
          </p>

          <a
            href={affiliateLink}
            target="_blank"
            className="bg-white text-black px-10 py-5 rounded-2xl font-bold text-lg"
          >
            Claim Hosting Discount
          </a>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="border-t border-zinc-800 py-10 text-center text-zinc-500">
        <p>
          © 2026 NexoraHost Affiliate Platform. All rights
          reserved.
        </p>
      </footer>
    </main>
  )
}
