const surgeSlider = document.getElementById('surge_multiplier');
const surgeReadout = document.getElementById('surge-readout');
const surgeBadge = document.getElementById('surge-badge');
const surgeScaleFill = document.getElementById('surge-scale-fill');

const distanceInput = document.getElementById('distance_km');
const seasonSelect = document.getElementById('season');
const dayTimeSelect = document.getElementById('day_time');

const routeDistanceLabel = document.getElementById('route-distance-label');
const chipDistance = document.getElementById('chip-distance');
const chipSeason = document.getElementById('chip-season');
const chipTime = document.getElementById('chip-time');

const MIN_SURGE = 1;
const MAX_SURGE = 3;

function surgeTier(v) {
  if (v < 1.5) return { name: 'calm', color: 'var(--accent-calm)' };
  if (v < 2.2) return { name: 'elevated', color: 'var(--accent-mid)' };
  return { name: 'peak', color: 'var(--accent-hot)' };
}

function updateSurgeUI() {
  const v = parseFloat(surgeSlider.value);
  const pct = ((v - MIN_SURGE) / (MAX_SURGE - MIN_SURGE)) * 100;
  const tier = surgeTier(v);

  surgeReadout.textContent = v.toFixed(2) + '×';
  surgeBadge.textContent = v.toFixed(2) + '× surge';
  surgeBadge.style.color = tier.color;
  surgeBadge.style.borderColor = tier.color;

  surgeScaleFill.style.width = Math.max(pct, 4) + '%';
}

function updateTripLabels() {
  const dist = parseFloat(distanceInput.value) || 0;
  routeDistanceLabel.textContent = dist + ' km trip';
  chipDistance.textContent = dist + ' km';
  chipSeason.textContent = seasonSelect.value;
  chipTime.textContent = dayTimeSelect.value;
}

surgeSlider.addEventListener('input', updateSurgeUI);
distanceInput.addEventListener('input', updateTripLabels);
seasonSelect.addEventListener('change', updateTripLabels);
dayTimeSelect.addEventListener('change', updateTripLabels);

updateSurgeUI();
updateTripLabels();

const form = document.getElementById('pricing-form');
const priceValue = document.getElementById('price-value');
const priceStatus = document.getElementById('price-status');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  priceStatus.textContent = 'Calculating fare...';
  priceStatus.className = 'fare-status';
  priceValue.textContent = '—';

  const payload = {
    demand: document.getElementById('demand').value,
    stock: document.getElementById('stock').value,
    competitor_price: document.getElementById('competitor_price').value,
    customer_rating: document.getElementById('customer_rating').value,
    discount: document.getElementById('discount').value,
    historical_sales: document.getElementById('historical_sales').value,
    distance_km: distanceInput.value,
    surge_multiplier: surgeSlider.value,
    season: seasonSelect.value,
    day_time: dayTimeSelect.value,
  };

  try {
    const res = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    const data = await res.json();

    if (data.success) {
      priceValue.textContent = '₹' + data.price.toLocaleString();
      priceStatus.textContent = 'Fare estimate ready';
      priceStatus.className = 'fare-status ok';
    } else {
      priceValue.textContent = '—';
      priceStatus.textContent = data.error || 'Prediction failed';
      priceStatus.className = 'fare-status error';
    }
  } catch (err) {
    priceValue.textContent = '—';
    priceStatus.textContent = 'Server error — is Flask running?';
    priceStatus.className = 'fare-status error';
  }
});