source "https://rubygems.org"

# Especifica la versión de Ruby que estás usando, opcional
ruby "2.7.4"

# Gema principal de Jekyll
gem "jekyll", "~> 4.3.0"

# Gema para la paginación
gem "jekyll-paginate", "~> 1.1.0"

# Otras gemas útiles para el desarrollo de Jekyll
gem "jekyll-sitemap", "~> 1.4.0" # Para generar un sitemap automáticamente
gem "jekyll-feed", "~> 0.15.1"   # Para generar un feed RSS automáticamente

# Gema para estilos SASS (si es necesario)
gem "jekyll-sass-converter", "~> 2.1"

# Si utilizas plugins de Jekyll administrados por GitHub Pages, puedes usar:
# gem "github-pages", group: :jekyll_plugins

# Grupo de desarrollo
group :jekyll_plugins do
  gem "jekyll-seo-tag", "~> 2.7" # Ayuda con las etiquetas SEO
end

# Para entorno de desarrollo (opcional)
group :development do
  gem "webrick", "~> 1.7" # Necesario para Jekyll en Ruby 3.0 y superior
end
