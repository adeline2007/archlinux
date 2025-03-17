-- КТО ОТКРЫЛ КОНФИГ - установи
-- yay -S clang pyright

-- Установка lazy.nvim
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", -- Используем стабильную версию
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- Настройки табуляции (4 пробела)
vim.opt.tabstop = 4      -- Количество пробелов, которые отображаются для табуляции
vim.opt.shiftwidth = 4   -- Количество пробелов для автоматических отступов
vim.opt.expandtab = true -- Преобразует табы в пробелы
vim.opt.smarttab = true  -- Умное использование табов

require("lazy").setup({
  -- Дерево файлов (nvim-tree)
  {
    "nvim-tree/nvim-tree.lua",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      require("nvim-tree").setup()
    end,
  },

  -- Автодополнение (nvim-cmp)
  {
    "hrsh7th/nvim-cmp",
    dependencies = {
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-vsnip",
      "hrsh7th/vim-vsnip",
    },
    config = function()
      local cmp = require("cmp")
      cmp.setup({
        snippet = {
          expand = function(args)
            vim.fn["vsnip#anonymous"](args.body)
          end,
        },
        mapping = {
          ["<C-b>"] = cmp.mapping(cmp.mapping.scroll_docs(-4), { "i", "c" }),
          ["<C-f>"] = cmp.mapping(cmp.mapping.scroll_docs(4), { "i", "c" }),
          ["<C-Space>"] = cmp.mapping(cmp.mapping.complete(), { "i", "c" }),
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_next_item({ behavior = cmp.SelectBehavior.Select })
            else
              fallback()
            end
          end, { "i", "s" }),
          ["<S-Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_prev_item()
            else
              fallback()
            end
          end, { "i", "s" }),
          ["<CR>"] = cmp.mapping.confirm({ select = false }), -- Не подтверждать по Enter
        },
        sources = cmp.config.sources({
          { name = "nvim_lsp" },
          { name = "vsnip" },
          { name = "buffer" },
          { name = "path" },
        }),
      })
    end,
  },

  -- LSP (Language Server Protocol)
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
    },
    config = function()
      require("mason").setup()
      require("mason-lspconfig").setup()
      require("lspconfig").pyright.setup({}) -- LSP для Python
      require("lspconfig").clangd.setup({})  -- LSP для C++
    end,
  },

  -- Запуск кода (vim-slime)
  {
    "jpalardy/vim-slime",
    config = function()
      vim.g.slime_target = "neovim"
      vim.g.slime_python_ipython = 1
    end,
  },

  -- Подсветка синтаксиса (nvim-treesitter)
  {
    "nvim-treesitter/nvim-treesitter",
    build = ":TSUpdate",
    config = function()
      require("nvim-treesitter.configs").setup({
        ensure_installed = { "python", "cpp" },
        highlight = {
          enable = true,
        },
      })
    end,
  },

  -- Цветовая схема (rose-pine)
  {
    "rose-pine/neovim",
    name = "rose-pine",
    lazy = false,
    priority = 1000,
    config = function()
      vim.cmd("colorscheme rose-pine")
    end,
  },

  -- Вкладки (barbar.nvim)
  {
    "romgrk/barbar.nvim",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function()
      require("barbar").setup()
    end,
  },

  -- Автоматическое закрытие скобок и кавычек (nvim-autopairs)
  {
    "windwp/nvim-autopairs",
    config = function()
      require("nvim-autopairs").setup({})
    end,
  },
})

-- Горячая клавиша для открытия дерева
vim.api.nvim_set_keymap('n', '<C-n>', ':NvimTreeToggle<CR>', { noremap = true, silent = true })

-- Команда для Python
vim.api.nvim_create_user_command('Runpy', function()
  vim.cmd('w')  -- Сохранить файл
  vim.cmd('!python ' .. vim.fn.expand('%:r') .. '.py') 
end, {})

-- Команда для С++
vim.api.nvim_create_user_command('Runcpp', function()
  vim.cmd('w')  -- Сохранить файл
  local filename = vim.fn.expand('%:r')  -- Имя файла без расширения
  vim.cmd('!g++ -o ' .. filename .. ' % && ./' .. filename)  -- Компиляция и запуск
end, {})

-- Горячие клавиши для управления вкладками
vim.api.nvim_set_keymap('n', '<A-,>', ':BufferPrevious<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<A-.>', ':BufferNext<CR>', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<A-c>', ':BufferClose<CR>', { noremap = true, silent = true })
